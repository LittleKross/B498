# Initialize frequency to 0
frequency = 0

# Open the file and store it in the data variable
data = open('Berkeley.csv')

# Remove the first header line
data.readline()

# Loop through each line of the file except the header
for line in data:
    
    # If the line contains Admitted in the first position and Female in the second position, the frequency is incremented
    if line.split(',')[0] == 'Admitted' and line.split(',')[1] == 'Female':
        frequency += 1
        
    # Print out each line
    print(line[:-1])
    
# Print out the frequency
print('Frequency of accepted females: ' + str(frequency))