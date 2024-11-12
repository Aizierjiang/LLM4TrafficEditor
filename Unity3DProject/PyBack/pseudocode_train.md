LoadData:
    Load CSV file
    Read image directory and steering angle values
    Resize the image to (sizeX, sizeY)
    Append image array to a list
    Split the data into train and validation sets

BuildModel:
    Create a sequential model
    Normalize input
    Add convolutional layers with ELU activation and specified strides
    Add a dropout layer
    Flatten the output
    Add dense layers with ELU activation
    Compile the model with mean squared error loss and Adam optimizer

Train:
    Define checkpoint for best model
    Compile the model with specified loss function and optimizer
    Fit the model on the training data with validation data and checkpoints