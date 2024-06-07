import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--specmaticJarPath", help="Location of the Specmatic jar file")

args = parser.parse_args()
jar_path = args.specmaticJarPath

if not jar_path:
    print("Please specify the location of the Specmatic jar file in the --specmaticJarPath parameter")
else:
    cmd = ["java", "-jar", jar_path, "test", "--host=127.0.0.1", "--port=5000"]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Print the output
    print(output.decode("utf-8"))
