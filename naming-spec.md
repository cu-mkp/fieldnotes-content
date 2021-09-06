# Naming spec for fieldnotes files and folders

`[semester]_[type]_[lastname]_[firstname]_[subject]`
delimited with + and - within each field

`[semester]` format:
\["fa" | "sp" | "su" ] + [YY]
e.g., "fa17" for fall 2017, or "sp16" for spring 2016, or "su21" for summer 2021

`[type]` values:
1) `fieldnotes`
2) `annotations`
3) `profiles`

## fieldnotes - directory structure and naming:

```
sp17/
	./fieldnotes/
		./van-buren_ariane/
			./sp17_fieldnotes_van-buren_ariane_verdigris.html
```

naming for any page without a specific person:
```
example_/
sp17_fieldnotes_example__verdigris.html
```

## annotations - directory structure and naming:
```
[semester]/
	./annotations/	
		./[annotation-subject]_[lastname+lastname]/
			./[semester]_annotations_[annotations-subject]_[lastname]_[subject].html
```

for example:
```
sp16/
	./annotations/	
		./distemper-and-shadows-beneath-skin_nisse/
			./sp16_annotations_distemper-and-shadows-beneath-skin_nisse_schematic-plan.html
```

