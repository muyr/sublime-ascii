# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.12
# Email : muyanru345@163.com
###################################################################

import sublime, sublime_plugin
import pickle, os

class AsciiCommand(sublime_plugin.TextCommand):  
    def run(self, args, f='#', e=' '): 
        view = self.view 
        selRegion = view.sel()[0]
        wordRegion = selRegion
        if selRegion.empty():
            wordRegion = view.word(selRegion)
        
        words = view.substr(wordRegion)
        edit = view.begin_edit()
        view.replace(edit, wordRegion, str2Ascii(words,f,e))
        view.end_edit(edit)
        # sublime.message_dialog("generate is success!")


class AsciisharpCommand(sublime_plugin.TextCommand):  
    def run(self, args):
        view = self.view
        selRegion = view.sel()[0]
        wordRegion = selRegion
        if selRegion.empty():
            wordRegion = view.word(selRegion)
        
        words = view.substr(wordRegion)
        edit = view.begin_edit()
        view.replace(edit, wordRegion, str2Ascii(words, '#'))
        view.end_edit(edit)


class AsciislashCommand(sublime_plugin.TextCommand):  
    def run(self, args):
        view = self.view
        selRegion = view.sel()[0]
        wordRegion = selRegion
        if selRegion.empty():
            wordRegion = view.word(selRegion)
        
        words = view.substr(wordRegion)
        edit = view.begin_edit()
        view.replace(edit, wordRegion, str2Ascii(words, '/'))
        view.end_edit(edit)

def str2Ascii(inputWord, fillChar = '#', emptyChar = ' '):
    if len(fillChar) != 1: fillChar = '#'
    if len(emptyChar) != 1: emptyChar = ' '
    pickleFile = open(os.path.expanduser(sublime.packages_path() + '\\Ascii\\asciiDict.mu'), 'rb')
    asciiDict = pickle.load(pickleFile)
    pickleFile.close()    
    outputWord = ''
    outputList = []
    for char in inputWord:
        if asciiDict.has_key(char.lower()):
            outputList.append(asciiDict.get(char.lower()))
    contentList = []
    for i in range(len(outputList[0])):
        tmpList = ''
        for j in range(len(outputList)):
            tmpList += outputList[j][i]
        contentList.append(tmpList)
    for i in contentList:
        for j in i:
            if j == '0':
                outputWord += emptyChar
            elif j == '1':
                outputWord += fillChar
        outputWord += '\n'
    return outputWord