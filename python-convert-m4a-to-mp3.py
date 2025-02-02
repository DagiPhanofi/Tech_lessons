#%% Convert .m4a files to .mp3 files
import os
#import logging
#import sys
import glob
import mutagen
from pydub import AudioSegment
#import ffmpeg

# Variables (set for your environment)
music_dir = os.path.join(os.path.expanduser("~"), "Downloads/Nao_songs")

# Get list of tags to update (they have to be supported by both mp3 and m4a/mp4 metadata)
from mutagen.easymp4 import EasyMP4Tags
from mutagen.easyid3 import EasyID3
#print('I am here')
allowed_mp3_tags = list(EasyID3.Set.keys())
allowed_m4a_tags = list(EasyMP4Tags.Set.keys())
tags_to_check = list(set.intersection(set(allowed_mp3_tags), set(allowed_m4a_tags)))

# Show the first message and then switch to showing only a single line
#switch_stdout_logger('perm')
#my_logger.info('Starting conversion scan of: %s' % music_dir)
#switch_stdout_logger('temp')

def short_file_name(file_name):
    return file_name.lstrip(music_dir)
def short_file_name_mp3(file_name):
    return file_name.lstrip(music_dir+'/mp3')
#print('I am also here')
# Iterate through .m4a files in 'music_dir'
os.chdir(music_dir)
#for m4a_file in glob.glob(music_dir + '/**/*.m4a', recursive=True):
for m4a_file in glob.glob(music_dir + '/*.m4a', recursive=True):    
    #print('I am in here')
    #my_logger.debug(r'm4a file: %s', short_file_name(m4a_file))
    #print(m4a_file)
    m4a_filename = short_file_name(m4a_file)
    #print(m4a_filename)
    mp3_filename = m4a_filename[:-4] + '.mp3'
    #mp3_file = m4a_file[:-4] + '.mp3'
    mp3_file = music_dir + '/mp3/' + mp3_filename
    if os.path.exists(mp3_file):
        #my_logger.info(r'mp3 file already exists: %s', short_file_name(mp3_file))
        print(r'mp3 file already exists:', short_file_name_mp3(mp3_file))
    else:
        try:
            # Create mp3 file
            #my_logger.info(r'Creating mp3 file: %s' % short_file_name(mp3_file))
            #print('I am in here before audiosegment')
            #print(short_file_name(mp3_file))
            #audio = AudioSegment.from_file(m4a_file,format='m4a')          
            audio = AudioSegment.from_file(m4a_file,format='m4a',start_second=24,duration=199)          

            audio.export(mp3_file, format='mp3')
            # Copy appropiate tags from m4a file to mp3 file
            #my_logger.debug(r'Reading file tags: %s' % short_file_name(m4a_file))
            m4a_tags = mutagen.File(m4a_file, easy=True)
            mp3_tags = mutagen.File(mp3_file, easy=True)
            for tag in tags_to_check:
                if tag in m4a_tags:
                    #my_logger.debug('writing tag %s: %s' % (tag, m4a_tags[tag]))
                    mp3_tags[tag] = m4a_tags[tag]
            mp3_tags.save()
        except Exception:
            #my_logger.exception('PROBLEM WITH CONVERTING: %s' % (short_file_name(m4a_file)))
            print('PROBLEM WITH CONVERTING: ', short_file_name(m4a_file))
            continue
print('Finished conversion of .m4a audio files to .mp3')
# Reset stdout formatter to show the final message
#switch_stdout_logger('perm')
#my_logger.info('Finished conversion scan of: %s' % music_dir)

# %%
