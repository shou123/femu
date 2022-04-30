from minio import Minio
import os


def clear():
        data_file_dir = '/home/fvm/info/datafile'
        for f in os.listdir(data_file_dir):
            os.remove(os.path.join(data_file_dir, f))
        download_file_dir = '/home/fvm/info/downloadfile'
        for f in os.listdir(download_file_dir):
            os.remove(os.path.join(download_file_dir, f))

        client = minio_server()
        objects = client.list_objects("bucket01")
        for obj in objects:
            client.remove_object("bucket01", obj.object_name)

def minio_server():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "10.0.2.15:9000",
        secure=False,
        access_key="minioadmin",
        secret_key="minioadmin",
    )
    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("bucket01")
    if not found:
        client.make_bucket("bucket01")

    return client

def main():
    clear()

if __name__ == "__main__":
    main()