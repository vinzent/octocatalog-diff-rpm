


```
rpmbuild -bb \
  --define "_topdir $(pwd)" \
  --define "_buildrootdir $BUILDROOT" \
  voxpupuli-octocatalog-diff.spec
```
