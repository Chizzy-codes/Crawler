import os


# Each website you crawl is a seperate project (Folder)
# site i want to crawl is crawler-test.com


def create_project_dir(directory: str):
    if not os.path.exists(directory):
        print(f"Creating project {directory}")
        os.makedirs(directory)

# Creating queue and crawled files (if not created)


def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

# sub function: create a new file


def write_file(path, data):
    with open(path, "w") as f:
        f.write(data)

# add data unto an existing file


def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the content of a file


def delete_file_content(path):
    with open(path, 'w'):
        pass

# read a file and convert each line into a set item while getting rid of the new line component of each line


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# iterate through a set, each item in the set will be a new line in the file:


def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)
