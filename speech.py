# -*- coding: utf-8 -*-

""" IMPORTS """
import speech_recognition as sr


""" SPEECH RECOGNITION """

def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)

    print(type(audio))
    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #   update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def sentence_transcription():
    num_sentences = 2
    prompt_limit = 2#nb of seconds waiting
    
    #Create recognizer and mic instances
    recognizer = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    microphone = sr.Microphone(device_index = 2, sample_rate = 44100, chunk_size = 512)

    for i in range(num_sentences):
        # get the sentence from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their guess again. Do this up
        #     to PROMPT_LIMIT times
        for j in range(prompt_limit):
            print("You can talk\n")
            sentence = recognize_speech_from_mic(recognizer, microphone)
            print(sentence)
            if sentence["transcription"]:
                break
            if not sentence["success"]:
                break
            print("I didn't catch that. What did you say?\n")
    
        # if there was an error, stop the game
        if sentence["error"]:
            print("ERROR: {}".format(sentence["error"]))
            break

        # show the user the transcription
        print("You said: {}".format(sentence["transcription"]))

        return sentence["transcription"]
