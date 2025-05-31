#Prompt the user for input — like they're speaking normally
spoken_input = input("Say something: ")

#Replace each space with "..." to simulate slow playback
playback_output = spoken_input.replace(" ", "...")

#Return the modified string
print(playback_output)