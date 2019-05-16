from sklearn import datasets
iris=datasets.load_iris()
iris_shape=iris.data.shape
print(iris_shape)
if iris_shape == (150,4):
	print("This Has Worked!")
else:
	print("Failed")
print(iris.data)
