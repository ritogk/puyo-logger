// main.js

// �A�v���P�[�V�����̎����̐���ƁA�l�C�e�B�u�ȃu���E�U�E�C���h�E���쐬���郂�W���[��
const { app, BrowserWindow } = require("electron")
const path = require("path")

// メインプロセス
const { desktopCapturer } = require("electron")

desktopCapturer
  .getSources({ types: ["window", "screen"] })
  .then(async (sources) => {
    for (const source of sources) {
      if (source.name === "Electron") {
        mainWindow.webContents.send("SET_SOURCE", source.id)
        return
      }
    }
  })

const createWindow = () => {
  // �u���E�U�E�C���h�E���쐬���܂��B
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  })

  // �����ăA�v���� index.html ��ǂݍ��݂܂��B
  mainWindow.loadFile("index.html")

  // �f�x���b�p�[ �c�[�����J���܂��B
  // mainWindow.webContents.openDevTools()
}

// ���̃��\�b�h�́AElectron �̏��������������A
// �u���E�U�E�C���h�E�̍쐬�������ł����Ƃ��ɌĂ΂�܂��B
// �ꕔ��API�͂��̃C�x���g������������ɂ̂ݗ��p�ł��܂��B
app.whenReady().then(() => {
  createWindow()

  app.on("activate", () => {
    // macOS �ł́ADock �A�C�R���̃N���b�N���ɑ��ɊJ���Ă���E�C���h�E���Ȃ�
    // �ꍇ�A�A�v���̃E�C���h�E���č쐬����̂���ʓI�ł��B
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
  })
})

// macOS �������A�S�E�C���h�E������ꂽ�Ƃ��ɏI�����܂��B ���[�U�[��
// Cmd + Q �Ŗ����I�ɏI������܂ŁA�A�v���P�[�V�����Ƃ��̃��j���[�o�[��
// �A�N�e�B�u�ɂ���̂���ʓI�ł��B
app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit()
})

// ���̃t�@�C���ł́A�A�v�����̂Ƃ��鑼�̃��C���v���Z�X�R�[�h��
// �C���N���[�h�ł��܂��B
// �ʁX�̃t�@�C���ɕ������Ă����� require ���邱�Ƃ��ł��܂��B
