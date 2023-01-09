import unreal

workingPath = "/Game/"


@unreal.uclass()
class MyEditorUtility(unreal.EditorAssetLibrary):
    pass


# Getting all the assets in the content browser
AssetLib = MyEditorUtility()
# list all the asset in the content browser
allAssets = AssetLib.list_assets(workingPath, True, False)

processingAssetPath = ""
allAssetsCount = len(allAssets)

if (allAssetsCount > 0):
    with unreal.ScopedSlowTask(allAssetsCount, processingAssetPath) as ST:
        ST.make_dialog(True)
        for asset in allAssets:
            processingAssetPath = asset
            deps = AssetLib.find_package_referencers_for_asset(asset, False)
            if (len(dep)<= 0):
                unreal.log(">>>>>>>>>>> Deleting >>>>>>>>>>>>   %s" % asset)
                AssetLib.delete_asset(asset)
            if ST.should_cancel():
                break
            ST.enter_progress_frame(1, processingAssetPath)