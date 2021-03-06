# AutoWalk
Configurable tool of bulking build path for AutoJump and Ranger.
There are `2` main usage you can choose:
- π **[ranger](https://github.com/ranger/ranger)** users: you can bulk build jump remap strings for your file system directories that you had set in autowalk configuration file.
- π **[autojump](https://github.com/wting/autojump)** users: you can also bulk increase | decrease | clear | list | clean autojump weights for your file system directories that you had set in autowalk configuration file.

## Requirements
You need to have the following:
- π₯ **Python3.6 +**
- π **[autojump](https://github.com/wting/autojump)** (Optional: If you only use Ranger to generate remap, don't need to install it).

## Installing
[πPyPI => AutoWalk ](https://pypi.org/project/autowalk/): 

- you can use `pip` to install it directly:

```shell
pip install autowalk
```

## Configuration file
π₯Notice: all the configuration options must be like π(No matter what the data type):
- outer: `List`
- inner: `string`
- between List: just `\n`

```python
xx = [
  "..."
]

xxx = [
  "..."
]
```

`~/.autowalk.py` is global config shared by Ranger and Autojump, you can set below:

- Common Configuration Option:
  - `recursion_root_list`: your filesystem paths that you want to add weights / remap
  - `recursion_depth`: control `recursion_root_list` depth of recursion
  - `black_list_dirname`: excluded paths that you don't what to be add weights / remap
  - `black_list_dirname_prefix`: similar to the above:  python's `str.startswith`
- Only for `AutoJump`
  - `weight_value_only_for_autojump`: the weight value of autojump
  - `autojump_default_config`: the path of autojump's `default` configuration file
- Only for `Ranger`
  - `prefix_and_suffix_only_for_ranger`: the format of ranger remap's name
  - `ranger_remap_output_file`: the output file location for ranger
  - `default_map_only_for_ranger`: some default remap for ranger

## USAGE
For convenience, command:  `aw`:
```shell
aw -h
```
### you can see help 
<a title="help">
  <img src="https://github.com/linusic/autowalk/blob/main/examples/0-autowalk-help.gif" width="600">
</a>

### you can see configuration file
<a title="configuration">
  <img src="https://github.com/linusic/autowalk/blob/main/examples/1-autowalk-config.png" width="600">
</a>

### you can see AutoJump
<a title="AutoJump">
  <img src="https://github.com/linusic/autowalk/blob/main/examples/2-1-bulk-add-weight-for-autojump.gif" width="600">
</a>

### you can see Ranger
<a title="Ranger">
  <img src="https://github.com/linusic/autowalk/blob/main/examples/2-2-bulk-generate-remap-for-ranger.gif" width="600">
</a>
