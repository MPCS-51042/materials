notebooks=$(find . -type f -name "*.ipynb")

for notebook in $notebooks
do
  jupyter nbconvert --clear-output --inplace $notebook
done
