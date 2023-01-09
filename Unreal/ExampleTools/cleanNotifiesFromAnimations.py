import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MyAnimationLibrary(unreal.AnimationLibrary):
    pass


Edutil = MyEditorUtility()
AnimLib = MyAnimationLibrary()


selectedAssets = Edutil.get_selected_assets()

for asset in selectedAssets:
    asset.modify(True)
    AnimLib.remove_all_animation_notify_tracks(asset)


