////////////////////////////////////////////////////////////////////////////////
/// Main
/// Mostly exists to avoid having global variables
/// Contains the data and methods that make CanvasStream function
////////////////////////////////////////////////////////////////////////////////
class Main {
    ////////////////////////////////////////////////////////////////////////////
    /// Constructor
    /// Execution begins here
    ////////////////////////////////////////////////////////////////////////////
    constructor() {
        this.events = [];
        this.sessionKey = "";
        this.time = "";
        this.canvas = document.getElementById("myCanvas")
        this.ctx = this.canvas.getContext("2d");
        this.imageCache = {};
        this.ctx.drawImg = function(imagePath, dx, dy, dWidth, dHeight) {
            const ctx = this;
            const imageCache = this.imageCache;
    
            const draw = function(ctx, imageCache, imagePath, dx, dy, dWidth, dHeight) {
                let args = [imageCache[imagePath], dx, dy];
                    if (dWidth != null && dHeight != null) {
                        args.push(dWidth);
                        args.push(dHeight);
                    }
                    ctx.drawImage.apply(ctx, args);
            }
    
            if (imagePath in this.imageCache) {
                draw(ctx, imageCache, imagePath, dx, dy, dWidth, dHeight)
            }
            else {
                const newImage = new Image();
                newImage.src = imagePath;
                this.imageCache[imagePath] = newImage;
                newImage.onload = function() {
                    draw(ctx, imageCache, imagePath, dx, dy, dWidth, dHeight);
                }
            }
        };

        this.ctx.drawImg.ctx = this.ctx;
        this.ctx.imageCache = {};
        // this.ctx.drawImg.imageCache = this.imageCache;
        


        
        this.framesPerSecond = 1000 / 30;

        this.setup();
        this.startEventLoop();
    }

    ////////////////////////////////////////////////////////////////////////////
    /// Setup
    /// Makes the initial connection to the server. Sets up the client to the
    /// initial starting state.
    ////////////////////////////////////////////////////////////////////////////
    setup() {
        const path = "/setup/";
        const type = "POST";
        const payload = {
            width: window.innerWidth,
            height: window.innerHeight,
            orientation: getOrientation()
        }
        
        const instructions = this.sendRequest(type, path, payload);
        this.processInstructions(instructions.instructions)
    }

    ////////////////////////////////////////////////////////////////////////////
    /// ProcessInstructions
    /// Executes the given instructions
    ///
    /// Parameters
    ///     instructions: Array[jsonObject]
    ///         An array of jsonObjects each with a type, name, and parameters
    ///         type: String, name: String, parameters: Array[String]
    ////////////////////////////////////////////////////////////////////////////
    processInstructions(instructions) {
        for (const instruction of instructions) {
            const type = instruction.type;
            const name = instruction.name;
            const parameters = instruction.parameters;
    
            if (type == "func") {
                this.ctx[name].apply(this.ctx, parameters);
            } else if (type == "var") {
                this.ctx[name] = parameters[0];
            } else if (type == "command") {
                if (name == "setWidth") {
                    this.canvas.width = parseInt(parameters[0]);
                } else if (name == "setHeight") {
                    this.canvas.height = parseInt(parameters[0]);
                } else if (name == "setSessionKey") {
                    this.sessionKey = parameters[0]
                } else if (name == "setListeners") {
                    this.registerEventListeners(parameters[0]);
                }
            }
        }
    }

    ////////////////////////////////////////////////////////////////////////////
    /// SendRequest
    /// Sends a request to the server 
    /// 
    /// Parameters
    ///     type: String 
    ///         Type of http request to make (GET, POST, etc)
    ///     path: String
    ///         Url to send reques to
    ///     payload: jsonObject
    ///         JSON to send to the server
    ///
    /// Returns
    ///     jsonObject
    ///         A json object recieved from the server. Will be null if failed 
    ////////////////////////////////////////////////////////////////////////////
    sendRequest(type, path, payload) {
        var xhr = new XMLHttpRequest();
        xhr.open(type, path, false); // Set the third parameter to true for asynchronous
        xhr.setRequestHeader('Content-Type', 'application/json');
        var postData = JSON.stringify(payload);
        xhr.send(postData);

        // Check the response status
        if (xhr.status === 200) {
            // Request was successful
            var responseText = xhr.responseText;
            return JSON.parse(responseText);
        } else {
            // Request failed
            console.error('POST Request failed with status:', xhr.status);
            return null;
        }
    }

    ////////////////////////////////////////////////////////////////////////////
    /// StartEventLoop
    /// Starts the event loop. Calls handle events for each frame. 
    ////////////////////////////////////////////////////////////////////////////
    startEventLoop() {
        this.handleEvents();
        self = this;
        setInterval(function() {
            self.handleEvents()
        }, 1000 / 30);
    }

    ////////////////////////////////////////////////////////////////////////////
    /// HandleEvents
    /// Sends the stored events to the server. Recieves instructions from the 
    /// server. Also increments the time and clears the stored events.
    ////////////////////////////////////////////////////////////////////////////
    handleEvents() {
        const type = "POST";
        const path = "/event/" + this.sessionKey;
        const payload = {
            events: this.events,
            time: this.time
        };
    
        // Send the POST request (blocking)
        const response = this.sendRequest(type, path, payload);
        this.processInstructions(response.instructions);

        this.time++;
        this.events = [];
    }

    ////////////////////////////////////////////////////////////////////////////
    /// RegisterEventListeners
    /// Adds the event listeners given in the array. 
    /// Parameters
    ///     listeners: Array[String]
    ///         Names of the event listeners to add 
    ///
    /// TODO: Refresh event listeners if server changes which ones are used.
    /// TODO: Add touch and controller events.
    /// TODO: Make sure click events work if canvas is resized.
    ////////////////////////////////////////////////////////////////////////////
    registerEventListeners(listeners) {
        if (listeners.includes("click")) {
            this.canvas.addEventListener('click', (event) => {
                this.events.push({
                    type: event.type,
                    x: event.clientX - this.canvas.getBoundingClientRect().left,
                    y: event.clientY - this.canvas.getBoundingClientRect().top,
                    ctrlKey: event.ctrlKey,
                    altKey: event.altKey,
                    metaKey: event.metaKey
                });
            });
        }
        
        if (listeners.includes("keydown")) {
            document.addEventListener('keydown', (event) => {
                this.events.push({
                    type: event.type,
                    ctrlKey: event.ctrlKey,
                    key: event.key,
                    shiftKey: event.shiftKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("keyup")) {
            document.addEventListener('keyup', (event) => {
                this.events.push({
                    type: event.type,
                    ctrlKey: event.ctrlKey,
                    key: event.key,
                    shiftKey: event.shiftKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("dblclick")) {
            this.canvas.addEventListener('dblclick', (event) => {
                this.events.push({
                    type: event.type,
                    x: event.clientX - this.canvas.getBoundingClientRect().left,
                    y: event.clientY - this.canvas.getBoundingClientRect().top,
                    ctrlKey: event.ctrlKey,
                    altKey: event.altKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("mousedown")) {
            this.canvas.addEventListener('mousedown', (event) => {
                this.events.push({
                    type: event.type,
                    x: event.clientX - this.canvas.getBoundingClientRect().left,
                    y: event.clientY - this.canvas.getBoundingClientRect().top,
                    ctrlKey: event.ctrlKey,
                    altKey: event.altKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("mouseup")) {
            this.canvas.addEventListener('mouseup', (event) => {
                this.events.push({
                    type: event.type,
                    x: event.clientX - this.canvas.getBoundingClientRect().left,
                    y: event.clientY - this.canvas.getBoundingClientRect().top,
                    ctrlKey: event.ctrlKey,
                    altKey: event.altKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("mousemove")) {
            this.canvas.addEventListener('mousemove', (event) => {
                this.events.push({
                    type: event.type,
                    x: event.clientX - this.canvas.getBoundingClientRect().left,
                    y: event.clientY - this.canvas.getBoundingClientRect().top,
                    ctrlKey: event.ctrlKey,
                    altKey: event.altKey,
                    metaKey: event.metaKey
                });
            });
        }
    
        if (listeners.includes("resize")) {
            window.addEventListener('resize', (event) => {
                this.events.push({
                    type: event.type,
                    width: window.innerWidth,
                    height: window.innerHeight,
                    orientation: getOrientation()
                });
            });
        }
    
        if (listeners.includes("beforeunload")) {
            window.addEventListener('beforeunload', () => {
                fetch("/disconnect/" + sessionKey)
            });
        }
    }
}

////////////////////////////////////////////////////////////////////////////////
/// GetOrientation
/// Gets the current orientation of the screen
///
/// Returns
///     String
///         PORTRAIT, LANDSCAPE, or UNKNOWN
////////////////////////////////////////////////////////////////////////////////
function getOrientation() {
    if (window.matchMedia("(orientation: portrait)").matches) {
        return "PORTRAIT"
    } else if (window.matchMedia("(orientation: landscape)").matches) {
        return "LANDSCAPE"
    }

    return "UNKNOWN"
}


// Start Execution
new Main();