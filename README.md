*Convert qb-inventory to qs-inventory.*

# Installation
  The preferred way is to use the executables located in releases, but should you wish to use the Python scripts, you will need [Python 3.9.15](https://www.python.org/downloads/release/python-3915/).

  If you wish to run it from source, you will need to do the following:
  
  `git clone https://github.com/CaptainStabs/qb-to-qs-inventory.git`
  
  `pip install -r requirements.txt`

# Important
  For all exported files, open them in a text editor, and make sure there is no `null` in them. If there is, do the following.

  Using find-and-replace:
  
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

   6. Import the CSV into `players` table in database. (I converted the csv into a sql insert statement)


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

  
  
