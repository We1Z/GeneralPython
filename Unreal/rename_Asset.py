import unreal

def renamer_assets():
    # instances of unreal classes 
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()
    
    # get teh selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0
    
    unreal.log("Selected {0} assets".format(num_assets))
    
    
renamer_assets()