# Naming spec for fieldnotes files and folders

`[semester]_[type]_[lastname]_[firstname]_[subject]`
delimited with + and - within each field

`[semester]` format:
\["fa" | "sp" | "su" ] + [YY]
e.g., "fa17" for fall 2017, or "sp16" for spring 2016, or "su21" for summer 2021

`[type]` values:
  1. `fld`
  2. `ann`
  3. `profiles`

## fieldnotes - directory structure and naming:

```
sp17/
	./fld/
		./van-buren_ariane/
			./sp17_fld_van-buren_ariane_verdigris.html
```

naming for any page without a specific person:
```
example_/
sp17_fld_example__verdigris.html
```

## annotations - directory structure and naming:
```
[semester]/
	./ann/
		./[annotation-subject]_[lastname+lastname]/
			./[semester]_ann_[annotations-subject]_[lastname]_[subject].html
```

for example:
```
sp16/
	./ann/	
		./distemper-and-shadows-beneath-skin_nisse/
			./sp16_ann_distemper-and-shadows-beneath-skin_nisse_schematic-plan.html
```

