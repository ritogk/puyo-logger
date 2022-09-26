// preload.js

// All the Node.js APIs are available in the preload process.
// Chrome �g���@�\�Ɠ����T���h�{�b�N�X�������Ă��܂��B
window.addEventListener("DOMContentLoaded", () => {
  const replaceText = (selector, text) => {
    const element = document.getElementById(selector)
    if (element) element.innerText = text
  }

  for (const dependency of ["chrome", "node", "electron"]) {
    replaceText(`${dependency}-version`, process.versions[dependency])
  }
})

// プリロードスクリプト内。
const { ipcRenderer } = require("electron")

ipcRenderer.on("SET_SOURCE", async (event, sourceId) => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: false,
      video: {
        mandatory: {
          chromeMediaSource: "desktop",
          chromeMediaSourceId: sourceId,
          minWidth: 1280,
          maxWidth: 1280,
          minHeight: 720,
          maxHeight: 720,
        },
      },
    })
    handleStream(stream)
  } catch (e) {
    handleError(e)
  }
})

function handleStream(stream) {
  console.log(1)
  const video = document.querySelector("video")
  video.srcObject = stream
  video.onloadedmetadata = (e) => video.play()
}

function handleError(e) {
  console.log(e)
}
