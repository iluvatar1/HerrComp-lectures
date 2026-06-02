.PHONY: book clean actions repo2docker binder devcontainer serve

book-lectures:
	@echo "Building and serving Jupyter Book..."
	bash nbgrader_and_sync.sh && \
	cd release && \
    rm -rf _build .jupyter_cache/&& \
	jupyter-book clean . && \
	jupyter-book build -v --all ./ && \
	cd _build/html && \
	python -m http.server 0

# book-lectures:
# 	@echo "Building lectures book with jupyter-book: run nbgrader and sync stuff, then cd into release, then build the book, then open it (note: this leaves the release dir modified, maybe a git checkout . is needed "
# 	bash nbgrader_and_sync.sh && \
# 	cd release && \
# 	jupyter-book build -v ./ && \
# 	open -a firefox _build/html/index.html && \
# 	git checkout .

book:
	@echo "Building book with jupyter-book"
	jupyter-book build -v ./

serve: book
	@echo "Serving Jupyter Book at http://localhost:8000"
	@cd _build/html && \
	python -m http.server 8000 & \
	sleep 1 && open http://localhost:8000


# Check https://github.com/nektos/act/issues/1658
actions:
	@echo "Running local actions"
	@echo "Do not forget to have docker running and also : sudo ln -s ~/.docker/run/docker.sock /var/run/docker.sock"
	act --secret-file .secrets -v --container-architecture linux/amd64

binder:
	@echo "Building binder image"
	docker build ./  -f ./Dockerfile  -t bindertest
	docker run -it --rm -p 8888:8888 bindertest jupyter notebook --NotebookApp.default_url=/lab/ --ip=0.0.0.0 --port=8888 --allow-root

repo2docker:
	@echo "Building docker image with repo2docker"
	repo2docker --user-id 1000 --user-name jovyan --debug --image-name r2d ./

devcontainer:
	@echo "Building and running  devcontainer image "
	devcontainer build --workspace-folder ./ --image-name devcontest
	docker run -it devcontest /bin/bash

nbgrader:
	@echo "Running nbgrader"
	nbgrader --version
	nbgrader generate_assignment --assignment="./lectures/*" --notebook="*" --force


clean:
	rm -f *~ #_build
