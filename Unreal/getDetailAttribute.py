import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


# selected asset from content browser
selectedAsset = MyEditorUtility().get_selected_assets()

# get the path of the asset
assetPathName = selectedAsset[0].get_path_name()

# load the assets
load_asset = unreal.load_asset(assetPathName)

for assetsLoaded in dir(load_asset):
    print(help(assetsLoaded))
