import os
from zipfile import ZipFile
import datetime
from sys import argv


def zip_with_dir(path, ziph):
    path_list = path.split(os.sep)[1:]

    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            root_list = root.split(os.sep)[1:]
            diff_list = list(set(root_list) - set(path_list))
            prefix = None

            if diff_list:
                prefix = diff_list[0]

            for file in files:
                filename = os.path.join(root, file)
                arcname = os.path.basename(filename)

                if prefix is not None:
                    arcname = os.path.join(prefix, arcname)

                ziph.write(filename, arcname)
    else:
        ziph.write(path, os.path.basename(path))


if __name__ == '__main__':
    src_path = argv[1]
    dst_path = argv[2]

    if os.path.exists(dst_path) and os.path.exists(src_path):
        target = src_path.split(os.sep)[-1:][0].lower()
        filepath = os.path.join(dst_path, target + str(datetime.date.today()) + '.zip')
        zipf = ZipFile(filepath, 'w')
        zip_with_dir(src_path, zipf)
        zipf.close()
