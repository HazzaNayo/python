from direct. showbase. ShowBase import ShowBase
from panda3d. core import loadPrcFile
from panda3d.core import DirectionalLight, AmbientLight
from panda3d.core import TransparencyAttrib
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import loadPrcFile, DirectionalLight, AmbientLight, TransparencyAttrib

loadPrcFile('settings.prc')

class MyGame(ShowBase):
    def __init__(self):
        super().__init__()
        self.load_models()
        self.setup_lights()
        self.setup_camera()

    def load_models(self):
        self.grassBlock = self.loader.loadModel('grass-block.glb')
        self.dirtBlock = self.loader.loadModel('dirt-block.glb')
        self.stoneBlock = self.loader.loadModel('stone-block.glb')
        self.sandBlock = self.loader.loadModel('sand-block.glb')

        self.grassBlock.reparentTo(self.render)
        self.grassBlock.setPos(-3, 10, 0)

        self.stoneBlock.reparentTo(self.render)
        self.stoneBlock.setPos(0, 10, 0)

        self.sandBlock.reparentTo(self.render)
        self.sandBlock.setPos(3, 10, 0)

        print("Model selesai dimuat.")

    def setup_lights(self):
        mainLight = DirectionalLight('main light')
        mainLightNodePath = self.render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        self.render.setLight(mainLightNodePath)

        ambientLight = AmbientLight('ambient light')
        ambientLight.setColor((0.3, 0.3, 0.3, 1))
        ambientLightNodePath = self.render.attachNewNode(ambientLight)
        self.render.setLight(ambientLightNodePath)
        print("Pencahayaan selesai diatur.")

    def setup_camera(self):
        print("Mengatur kamera ...")
        self.camera.setPos(0, 0, 3)
        self.camLens.setFov(80)

        crosshairs = OnscreenImage(image='crosshairs.png', pos=(0, 0, 0), scale=0.05)
        crosshairs.setTransparency(TransparencyAttrib.MAlpha)


if __name__ == '__main__':
    game = MyGame()
    game.run()