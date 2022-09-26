var log = require("electron-log")
process.on("uncaughtException", function (err) {
  log.error("electron:event:uncaughtException")
  log.error(err)
  log.error(err.stack)
  app.quit()
})

const { app, BrowserWindow } = require("electron")
const path = require("path")
let win

function createWindow() {
  //ウインドウの作成
  win = new BrowserWindow({
    width: 800,
    height: 800,
    webPreferences: {
      nodeIntegration: true, //デフォルト設定だとレンダープロセスとメインプロセスで通信できない。trueでできるようになる
      preload: path.join(__dirname, "preload.js"),
    },
  })

  //ウインドウに表示する内容
  win.loadFile("index.html")

  //デバッグ画面表示
  win.webContents.openDevTools()

  //このウインドウが閉じられたときの処理
  win.on("closed", () => {
    win = null
  })
}

//アプリが初期化されたとき（起動されたとき）
app.on("ready", () => {
  createWindow()
})

//全ウインドウが閉じられたとき
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit()
  }
})

//アクティブになったとき（MacだとDockがクリックされたとき）
app.on("activate", () => {
  if (win === null) {
    createWindow()
  }
})

// メインプロセス
const { desktopCapturer } = require("electron")

// desktopCapturer
//   .getSources({ types: ["window", "screen"] })
desktopCapturer.getSources({ types: ["window"] }).then(async (sources) => {
  for (const source of sources) {
    if (source.name === "Puyo Puyo Champions") {
      console.log(source)
      win.webContents.send("SET_SOURCE", source.id)
      return
    }
  }
})
