import sys
import os
import aiml as aimlLib


def generateBot(aiml,brn):
    
    if aiml[-5:] != '.aiml':
        print('Bot definition file does not have the aiml extension')
        sys.exit(-2)
    if brn[-4:] != '.brn':
        print('Bot brain output file does not have the brn extension')
        sys.exit(-3)
    if not os.path.isfile(aiml):
        print('Bot definition file does not exist')
        sys.exit(-4)

    kernel = aimlLib.Kernel()

    kernel.learn(aiml)
    kernel.saveBrain(brn)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: botDefinition botBrainOutputPath')
        sys.exit(-1)
    generateBot(sys.argv[1],sys.argv[2])