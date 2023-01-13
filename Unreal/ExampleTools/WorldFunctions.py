import unreal

@unreal.uclass()
class MyEditorUtil(unreal.GlobalEditorUtilityBase):
    pass

MyEditorUtil.get


def focusViewportOnActor(active_viewport_only=True, actor=None):
    command = 'CAMERA ALIGN'
    if active_viewport_only:
        command += ' ACTIVEVIEWPORTONLY'
    if actor:
        command += ' NAME=' + actor.get_name()
    executeConsoleCommand(command)


# console_command: str : The console command
def executeConsoleCommand(console_command=''):
    unreal.CppLib.execute_console_command(console_command)

focusViewportOnActor(True, None)
