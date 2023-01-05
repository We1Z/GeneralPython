import unreal

totalFrames = 500
textDisplay = "I love python, and I will be using this as an example"

with unreal.ScopedSlowTask(totalFrames, textDisplay) as ST:
    ST.make_dialog(True)
    for i in range(totalFrames):

        # checking whether user have cancel the task
        if ST.should_cancel():
            break

        # if user didnt cancel the task then continue with the for loop
        unreal.log(f"{i} steps!!!")
        # make progress bar move
        ST.enter_progress_frame(1)
