import unreal

materialName = ""
materialFilePath = ""


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


@unreal.uclass()
class MyMaterialLibrary(unreal.MaterialEditingLibrary):
    pass


# selected the material
selectedMaterial = MyEditorUtility().get_selected_assets()

for asset in selectedMaterial:
    materialName = asset.get_name()
    materialFilePath = asset.get_path_name()

    unreal.log(materialName)
    unreal.log(materialFilePath)

    loadMaterial = unreal.load_asset(materialFilePath)
    unreal.log(loadMaterial)

    MyMaterialLibrary.get_material_selected_nodes(asset)








# find specific node
# checking master material whether has runtime virtual texture output node
