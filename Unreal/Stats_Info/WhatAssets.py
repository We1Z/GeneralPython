import unreal


@unreal.uclass()
# decorators are required to correctly expose classes, functions and properties to Unreal's refelction system, and provide Unreal specific metadata
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


# Now if there is anything selected in the content browser, we will get it in a array
selectedAssets = MyEditorUtility().get_selected_assets()

for asset in selectedAssets:
    #unreal.log("There are something selected")
    unreal.log(asset.get_name())
    unreal.log(asset.get_full_name())
    unreal.log(asset.get_path_name())
    unreal.log(asset.get_class())

    unreal.log("**********************************")


