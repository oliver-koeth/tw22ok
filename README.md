# Tech Week Streamlit Talk

## Presentation Flow

### Working with Notebooks

```
https://colab.research.google.com
```

Open a new notebook and print "Hello world"

#### Hello Notebook World

Open HelloNotebook

```
import matplotlib.pyplot as plt

plt.plot([72,26,22,40,58,70])
plt.ylabel('My COVID HRV')

plt.show()
```

#### Data Visualisation Notebook

Open file: `HelloGPX-1.ipynb`

```
import sys
!{sys.executable} -m pip install gpxpy
```

### Working with Streamlit

#### Hello Streamlit

Open file: `tw22ok_hello_streamlit.py`

Run `streamlit run tw22ok_hello_streamlit.py`

Link to documentation: [Streamlit Docs](https://docs.streamlit.io)

```
if st.checkbox('Show result'):
```

#### Data Visualisation with Streamlit

Open file: `tw22ok_hello_GPX.py`

Run `streamlit run tw22ok_hello_GPX.py`

#### Deploy on Streamlit Cloud

TODO: Deployment Workflow, Check update

#### Example for a real application

Open page [Streamlit App](https://oliver-koeth-pacer-lit-pacer-lit-9n25j7.streamlitapp.com)

## Setup Local Streamlit Env in Conda
When running for the first time, create a respective conda environment. In case
of doubt whether a conda environment exists, you can list all environments
(the environment for this project is called `tw22ok-env`, the environment file 
uses the extension `.local` so that Stremalit.io cloud does not get confused.):
```
conda env list
conda env create -f environment.yml
conda activate tw22ok-env
pip install -r requirements.txt
```

Now run:
```
streamlit run tw22ok_hello_streamlit.py
```

To eventually remove the environment run:
```
conda deactivate
conda remove --name tw22ok-env --all
```

