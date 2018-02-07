/* eslint-disable */
var userCode;

var prefixCode = 'from cira.cirainput import *\n' +
  'from cira.ciradisplay import *\n' +
  'from ciraweb.coreinputweb import *\n' +
  'from ciraweb.coredisplayweb import *\n' +
  '\n';

var suffixCode = '\n' +
  'myCoreInput = CoreInputWeb()\n' +
  'myCiraInput = CiraInput(myCoreInput)\n' +
  '\n' +
  'myCoreDisplay = CoreDisplayWeb()\n' +
  'myCiraDisplay = CiraDisplay(myCoreDisplay)\n' +
  '\n' +
  'game = MyGame(myCiraInput, myCiraDisplay)\n' +
  '\n' +
  'def gameEvent():\n' +
  '    if myCoreInput.shouldQuit():\n' +
  '        print("quitting")\n' +
  '    else:\n' +
  '        game.gameStep()\n' +
  '\n';

function MakeLog() {
}

function LogSuccess() {
  alert("Success!");
}

function LogFail() {
  alert("Failure to save");
}

function SkulptWrite(text) {
  var output = document.getElementById("outputLog");
  output.innerHTML = output.innerHTML + text;
  output.scrollTop = output.scrollHeight;
}

export function SkulptClearPrints() {
  var output = document.getElementById("outputLog");
  output.innerHTML = '';
}

export function SkulptClearScreen() {
  var python = 'import cirawebjs\n' +
    'display = cirawebjs.Display()\n' +
    'for col in range(20):\n' +
    '    for row in range(23):\n' +
    '        display.setPixel(col, row, 0, 0, 0)\n';
  SkulptRunSnippet(python);
}

function SkulptRead(x) {
  if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
    throw "File not found: '" + x + "'";
  return Sk.builtinFiles["files"][x];
}

export function SkulptRun(x) {
  MakeLog()
  //simulate stop button if needed
  var timeOut = 1;
  if (!shouldQuit) {
    SkulptClearScreen();
    SkulptQuit();
    SkulptClearPrints();
    timeOut = 110;
  }
  //wait for screen to clear before restarting
  setTimeout(function () {
    shouldQuit = false;
    var mycanvas = document.getElementById("game");
    mycanvas.getContext('2d').clearRect(0, 0, mycanvas.width, mycanvas.height);
    SkulptClearScreen();
    //Colors for BG and border of cira light emulator after run has been pressed?
    //mycanvas.style.border = "1px solid #000";
    //mycanvas.style.backgroundColor = "#000";
    Sk.configure({ output: SkulptWrite, read: SkulptRead });
    Sk.canvas = "game";
    Sk.pre = "outputLog";
    try {
      var codeText = prefixCode + x + suffixCode;
      userCode = Sk.importMainWithBody("<stdin>", false, codeText);
      RunLoop();
    } catch (e) {
      console.error(e);
      WriteError(e.toString());
    }
  }, timeOut);
}

function SkulptRunSnippet(x) {
  shouldQuit = false;
  Sk.configure({ output: SkulptWrite, read: SkulptRead });
  Sk.canvas = "game";
  Sk.pre = "outputLog";
  try {
    var codeText = x;
    Sk.importMainWithBody("<stdin>", false, codeText);
  } catch (e) {
    WriteError(e.toString());
  }
}

export function SkulptQuit() {
  shouldQuit = true;
  var mycanvas = document.getElementById("game");
  //Colors for BG and border of cira light emulator after run has been pressed?
  //mycanvas.style.border = "1px solid #FFF";
  //mycanvas.style.backgroundColor = "#FFF";
}

var minFrameTime = 40;
var lastFrameTime;
var shouldQuit = true;

function GetTime() {
  var timer = new Date();
  return timer.getTime();
}

function RunLoop() {

  var gameEvent = userCode.tp$getattr('gameEvent');

  var mainLoop = function () {
    var currentTime = GetTime();
    if (currentTime - lastFrameTime >= minFrameTime) {
      Sk.misceval.callsim(gameEvent);
      lastFrameTime = GetTime();
    }
  };

  var animFrame = window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.oRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    null;

  if (animFrame !== null) {
    lastFrameTime = GetTime();
    var recursiveAnim = function () {
      if (!shouldQuit) {
        mainLoop();
        animFrame(recursiveAnim);
      }
    };

    animFrame(recursiveAnim);
  } else {
    var ONE_FRAME = 1000.0 / 60.0;
    setInterval(mainloop, ONE_FRAME);
  }
}

function WriteError(errorMsg) {
  //Find the line number at end of "error blah blah at line ##", correct it down, and add it back
  var numberPos = errorMsg.lastIndexOf("line");
  if (numberPos != -1) {
    numberPos += 5; //add length of "line "
    var errorLine = parseInt(errorMsg.substring(numberPos));
    var lineOffset = (prefixCode.match(/\n/g) || []).length;
    errorLine = errorLine - lineOffset;

    //format the error msg
    errorMsg =
      "<strong style='color: red;'>" +
      "-------ERROR on line " + errorLine + "-------------\n" +
      "</strong>" +
      errorMsg.substring(0, numberPos) + (errorLine) + '\n' +
      "<strong style='color: red;'>" +
      "--------------------------------------\n" +
      "</strong>";
  }
  else {
    //No line number given, so generic error msg
    errorMsg =
      "<strong style='color: red;'>" +
      "--------------ERROR-------------------\n" +
      "</strong>" +
      errorMsg + '\n' +
      "<strong style='color: red;'>" +
      "--------------------------------------\n" +
      "</strong>";
  }

  //Output the error message!
  SkulptWrite(errorMsg);
}
