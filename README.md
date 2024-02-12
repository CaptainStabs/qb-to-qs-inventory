*Convert qb-inventory to qs-inventory.*

# Installation
  The preferred method of installation is to use the executables located in the [releases](https://github.com/CaptainStabs/qb-to-qs-inventory/releases) section. However, if you prefer using the Python scripts, make sure you have [Python 3.9.15](https://www.python.org/downloads/release/python-3915/) installed.

  If you want to run the converter from the source code, follow these steps:
  
  ```
  git clone https://github.com/CaptainStabs/qb-to-qs-inventory.git
  cd qb-to-qs-inventory
  pip install -r requirements.txt
  ```

# Important Note
  After exporting the files from the database, open them in a text editor and ensure there is no null present. If found, perform the following replacements using find-and-replace:
  
    ,null, -> ,

    [null, -> [

# Inventory Conversion
  1. Run query
     ```sql
      SELECT citizenid, inventory FROM players;
      ```

  2. Export result with [TablePlus](https://tableplus.com/) **(Preferred over HeidiSQL, HeidiSQL export is untested)**, using the following settings
     ![image](https://github.com/CaptainStabs/qb-to-qs-inventory/assets/40151222/e83e8f98-6cc5-4bf2-ab43-52fda04b4a60)
  
  3. Move the exported file into the same working directory as `player_converter.exe`
  5. In the command line, run `player_converter.exe <filename>`

     The default filename is `players.csv`, so if you named it that, you can just run `player_converter.exe`
     If you are running them through Python, do `python player_converter.py <filename>`

   6. Import the CSV into `players` table in database. (I converted the csv into a sql update statement)


# Stash Conversion
  1. Run query
     ```sql
     SELECT * FROM stashitems;
     ```

  2. Export the results as before, following steps 2-3 for inventory conversion
  3. In the command line, run `stash_converter.exe <filename>`

     Default filename is `stashitems.csv`
  4. Import into `inventory_stash`


# Trunk conversion
  1. Run query
     ```sql
     SELECT * FROM trunkitems;
     ```

  2. Export the results.
  3. In the command line, run `trunk_glove_converter.exe <filename>`
  4. Import the resulting file into `inventory_trunk` table

# Glovebox Conversion
  1. Run query
     ```sql
     SELECT * FROM gloveboxitems;
     ```
  2. Export the results
  3. In the commandline, run `trunk_glove_converter.exe <filename>`
  4. Import the resulting file into `inventory_glovebox`

  # Building from Source
  1. Clone the repo and CD into each tool individually
  2. Run the following, replacing the path with the path to the numpy binary `libopenblas64__v0.3.23-293-gc2f4bdbb-gcc_10_3_0-2bde3a66a51006b2b53eb373ff767a3f.dll` (or whatever it is for your version):
```
pyinstaller --onefile --add-binary="C:/Users/User/miniconda3/envs/converter/Lib/site-packages/numpy.libs:." <script>
```
  
