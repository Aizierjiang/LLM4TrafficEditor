## Run the following 2 commands manually first
# conda create --name pyudacity python=3.7
# activate pyudacity

# Following commands can be run automatically
conda install -c anaconda jupyter
pip install ipykernel
python -m ipykernel install --user --name pyudacity --display-name "pyudacity"
conda install -c anaconda tensorflow-gpu
pip uninstall tensorflow -y
pip install tensorflow==2.3.0
pip install keras==2.4

pip install pillow
pip install opencv-python
pip install pandas
pip install scikit-learn

