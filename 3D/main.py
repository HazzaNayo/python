import os
import sys
from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename, AmbientLight, DirectionalLight, Vec4, Vec3, NodePath, ClockObject


class GLBViewer(ShowBase):
    def __init__(self, glb_filename="residential_buildings_by_the_river_and_bridge.glb"):
        ShowBase.__init__(self)

        # resolve path to model
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, glb_filename)
        if not os.path.exists(path):
            print(f"GLB file not found: {path}")
            sys.exit(1)

        # load model
        self.model = self.loader.loadModel(Filename.fromOsSpecific(path))
        self.model.reparentTo(self.render)
        self.model.setPos(0, 5, 0)    # move model in front of camera
        self.model.setScale(1)

        # camera
        self.camera.setPos(0, -12, 3)
        self.camera.lookAt(self.model)

        # lights
        ambient = AmbientLight("ambient")
        ambient.setColor(Vec4(0.4, 0.4, 0.4, 1))
        ambient_np = self.render.attachNewNode(ambient)
        self.render.setLight(ambient_np)

        directional = DirectionalLight("directional")
        directional.setColor(Vec4(1, 1, 1, 1))
        directional_np = self.render.attachNewNode(directional)
        directional_np.setHpr(-30, -60, 0)
        self.render.setLight(directional_np)

        # exit on Escape
        self.accept("escape", sys.exit)
        
        

if __name__ == "__main__":
    # optionally allow passing a different filename via command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "residential_buildings_by_the_river_and_bridge.glb"
    viewer = GLBViewer(filename)
    viewer.run()