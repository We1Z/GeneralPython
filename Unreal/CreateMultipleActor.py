# The Following code is going operate like if you are dragging assets from content browser into the world outline
import unreal

actorsCount = 50
slowTaskDisplayText = "We are creating actor in the scene"


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


selectedAssets = MyEditorUtility().get_selected_assets()

with unreal.ScopedSlowTask(actorsCount, slowTaskDisplayText) as ST:
    ST.make_dialog(True)
    for i in range(actorsCount):
        if ST.should_cancel():
            break
        unreal.EditorLevelLibrary.spawn_actor_from_object(selectedAssets[0], unreal.Vector(1.0+ i*100 , 1.0+ i*100, 0.0),
                                                              unreal.Rotator(0.0, 0.0, 0.0))
        unreal.log("Just added an actor to the level!")
        ST.enter_progress_frame(1)

