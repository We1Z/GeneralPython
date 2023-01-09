import unreal


@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass


selectedActors = MyEditorUtility().get_selection_set()

for actor in selectedActors:
    unreal.log(actor.get_name())
    #unreal.log(actor.get_fname())
    if actor.actor_has_tag("tagOne"):
        unreal.log("[1]")
    if actor.actor_has_tag("tagTwo"):
        unreal.log("[2]")
    if actor.actor_has_tag("tagThree"):
        unreal.log("[3]")
    if actor.actor_has_tag("tagFour"):
        unreal.log("[4]")
    unreal.log("**********************************")

