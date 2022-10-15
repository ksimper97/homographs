def split_path(path):
  ''' Split Path

  Splits a path by its slashes and returns a list
  of all significant path parts
  '''
  # Standardize slashes
  path = path.replace("\\", "/")

  # Split at slashes
  path_parts = path.split("/")

  # Sort out the empty parts
  actual_parts = []
  for part in path_parts:
    if part != "":
      actual_parts.append(part)

  return actual_parts

def canonizerize(path, cwd = "C:/Program Files/Some Company/Random Program Folder/"):
  
  ''' Canonicalization Function
  
  Returns a path's canonical form
  '''
  
  # Get the listified current working directory
  cwd = cwd.lower()
  cwd_parts = split_path(cwd)

  # Get the listified path
  path = path.lower()
  parts = split_path(path)

  # Need to handle just the file name

  if path[0] in ["/", "\\"]:
    # Handles /test/file.txt == C:/test/file.txt
    # An absolute path from cwd letter drive
    parts = cwd_parts[0] + parts
  
  elif ":" in parts[0]:
    # Handles C:test/file.txt == C:/test/file.txt
    first_part = parts[0].split(":")
    # Remove the first part
    parts.pop(0)
    # Replace it with its split parts
    parts.insert(0, first_part[1])
    parts.insert(0, first_part[0] + ":")

  else:
    # Handles all other cases of relative paths
    parts = cwd_parts + parts

  new_list = []
  for part in parts:
    if part == ".":
      # Ignore
      continue
    elif part == "..":
      # Backtrack the path, but always maintain the letter drive
      if len(new_list) > 1:
        new_list.pop()
    else:
      # Add onto canon
      new_list.append(part)


  print(new_list)
  return new_list


def check_homographs(path1, path2):
  # Canonicalize
  path1 = canonizerize(path1)
  path2 = canonizerize(path2)

  # Compare and return
  if path1 == path2:
    return True
  else:
    return False
  


def test(path1, path2, expected_result):
  ''' Run Test

  Displays and runs a test
  '''
  # Display Test
  print("Testing:")
  print(f"Path 1: ${path1}")
  print(f"Path 2: ${path2}")
  print()
  if expected_result:
    print("Assert(Path1 == Path2)")
  else:
    print("Assert(Path1 != Path2)")

  # Run Test
  if check_homographs(path1, path2) == expected_result:
    print("Passed!")
  else:
    print("FAIL")


def run_tests():
  #Non homographs
  print("Non-Homograph Test Cases\n")
  test(
    "C:/Program Files/Some Company/Random Program Folder/test.txt",
    "C:/Program Files/Some Company/test.txt",
    False
  )
  test(
    "C:/Program Files/Some Company/test.txt",
    "./test.txt",
    False
  )
  test(
    "C:/Program Files/Secret Folder/test.txt",
    "../../test.txt",
    False
  )
  test(
    "C:/Program Files/Secret Folder/test.txt",
    "C:/Program Files/test.txt",
    False
  )
  test(
    "C:/Program Files/Secret Folder/test.txt",
    "../../../../../../../../Program Files/test.txt",
    False
  )
  test(
    "C:/Program Files/Secret Folder/test.txt",
    "/test.txt",
    False
  )









  #Homographs
  print("Homograph Test Cases\n")
  test(
    "C:/Program Files/Some Company/Random Program Folder/../Random Program Folder/test.txt",
    "C:/Program Files/Some Company/Random Program Folder/test.txt",
    True
  )
  test(
    "./test.txt",
    "test.txt",
    True
  )
  test(
    '../../../Program Files/Some Company/Random Program Folder/test.txt',
    '../Random Program Folder/test.txt',
    True
  )
  test(
    './././././././././././././././././././././././././././././././././././test.txt',
    'test.txt',
    True
  )
  test(
    './../Random Program Folder/./../../Some Company/Random Program Folder/test.txt',
    'test.txt',
    True
  )
  test(
    '../../../../../../../../../../../../../../../../../../../../Program Files/Some Company/Random Program Folder/test.txt',
    'test.txt',
    True
  )

def menu():
  check = input('1. Run Test\n2. Compare Two File Paths\n(q) Quit\n')
  
  if check == '1':
    run_tests()
    print('')
    menu()
  elif check == '2':
    path1 = input("Input first filepath: ")
    path2 = input("Input second filepath: ")
    if check_homographs(path1,path2):
      print("The filepaths are homographs\n")
    else:
      print("The filepaths are not homographs\n")
    menu()
  elif check == "q" or check == "Q" or check == "quit":
    pass
  else:
    print("Input Error")
    menu()


def main():
  # Menu
  menu()
  
    
  # 1. run test

  # 2. compare file paths
  # (q) quit
  #
  # ?:
  '''
  path1 = "/////hello"
  path2 = "C:/Users/../Users/smith"
  path3 = "./../homographs"
  path4 = "./////../homographs/////./././././././././././././././."
  path5 = "./../../../../../../../../../../Users/smith/.gitconfig"
  path6 = "../homograph/secret.txt"
  canonizer(path1)
  canonizer(path2)
  canonizer(path3)
  canonizer(path4)
  canonizer(path5)
  canonizer(path6)
  '''




if __name__ == "__main__":
  main()