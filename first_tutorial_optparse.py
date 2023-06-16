from optparse import OptionParser
import random
# Initialize the parser
parser = OptionParser()


# Seed for random number generator
parser.add_option('-s', '--seed', dest='seed', help='seed for random number generator', default=0, type='int', action='store')
(options, args) = parser.parse_args()
print('seed: %d' % (options.seed))
#  the code sets the seed to the specified value, ensuring that the sequence of-
# random numbers generated afterwards will be the same for each run of the program with the same seed value.
random.seed(options.seed)

# generate a random number
print('random number: %f' % (random.random()))
