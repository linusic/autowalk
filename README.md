# autowalk
Configurable tool of bulking build path for AutoJump and Ranger.
There are `2` main usage you can choose:
- 🚀 **[ranger](https://github.com/ranger/ranger)** users: you can bulk build jump remap strings for your file system directories that you had set in autowalk configuration file.
- 🚀 **[autojump](https://github.com/wting/autojump)** users: you can also bulk increase | decrease | clear | list | clean autojump weights for your file system directories that you had set in autowalk configuration file.

## Requirements
You need to have the following:
- 🔥 **Python3.6 +**
- 🚀 **[autojump](https://github.com/wting/autojump)** (Optional: If you only use Ranger to generate remap, you don't need to install it).

## Installing
[🚀PyPI => AutoWalk ](https://pypi.org/project/autowalk/): 

- you can use `pip` to install it directly:

```shell
pip install autowalk
```

## Configuration file
🔥Notice: all the configuration options must be like 👇(No matter what the data type):
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

`~/.autowalk.py` is global config, and shared by Ranger options and Autojump options
and you can set below:

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

<a title="help" href="">
  <img src="https://i.imgur.com/vtG8olE.png](https://github.com/linusic/autowalk/blob/main/examples/0-autowalk-help.gif" width="640">
</a>
