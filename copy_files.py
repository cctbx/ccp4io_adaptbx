import sys, os
op = os.path

def run(args):
  assert len(args) == 1
  source_root = args[0]
  relative_paths = """\
lib/data/syminfo.lib
lib/data/symop.lib
lib/src/binsort.h
lib/src/binsortint.c
lib/src/ccp4_array.c
lib/src/ccp4_array.h
lib/src/ccp4_diskio_f.c
lib/src/ccp4_errno.h
lib/src/ccp4_file_err.h
lib/src/ccp4_fortran.h
lib/src/ccp4_general.c
lib/src/ccp4_general.h
lib/src/ccp4_general_f.c
lib/src/ccp4_parser.c
lib/src/ccp4_parser.h
lib/src/ccp4_parser_f.c
lib/src/ccp4_program.c
lib/src/ccp4_program.h
lib/src/ccp4_spg.h
lib/src/ccp4_sysdep.h
lib/src/ccp4_types.h
lib/src/ccp4_unitcell.c
lib/src/ccp4_unitcell.h
lib/src/ccp4_unitcell_f.c
lib/src/ccp4_utils.h
lib/src/ccp4_vars.h
lib/src/cmap_accessor.c
lib/src/cmap_close.c
lib/src/cmap_data.c
lib/src/cmap_data.h
lib/src/cmap_errno.h
lib/src/cmap_header.c
lib/src/cmap_header.h
lib/src/cmap_labels.c
lib/src/cmap_labels.h
lib/src/cmap_open.c
lib/src/cmap_skew.c
lib/src/cmap_skew.h
lib/src/cmap_stats.c
lib/src/cmap_stats.h
lib/src/cmap_symop.c
lib/src/cmaplib.h
lib/src/cmaplib_f.c
lib/src/cmaplib_f.h
lib/src/cmtzlib.c
lib/src/cmtzlib.h
lib/src/cmtzlib_f.c
lib/src/csymlib.c
lib/src/csymlib.h
lib/src/csymlib_f.c
lib/src/cvecmat.c
lib/src/cvecmat.h
lib/src/fftlib.f
lib/src/library_err.c
lib/src/library_f.c
lib/src/library_f.h
lib/src/library_file.c
lib/src/library_file.h
lib/src/library_utils.c
lib/src/mtzdata.h
lib/src/overview.h
lib/src/pack_c.c
lib/src/pack_c.h
lib/src/mmdb/bfgs_min.cpp
lib/src/mmdb/bfgs_min.h
lib/src/mmdb/file_.cpp
lib/src/mmdb/file_.h
lib/src/mmdb/hybrid_36.cpp
lib/src/mmdb/hybrid_36.h
lib/src/mmdb/linalg_.cpp
lib/src/mmdb/linalg_.h
lib/src/mmdb/machine_.cpp
lib/src/mmdb/machine_.h
lib/src/mmdb/math_.cpp
lib/src/mmdb/math_.h
lib/src/mmdb/mattype_.cpp
lib/src/mmdb/mattype_.h
lib/src/mmdb/mmdb_align.cpp
lib/src/mmdb/mmdb_align.h
lib/src/mmdb/mmdb_atom.cpp
lib/src/mmdb/mmdb_atom.h
lib/src/mmdb/mmdb_bondmngr.cpp
lib/src/mmdb/mmdb_bondmngr.h
lib/src/mmdb/mmdb_chain.cpp
lib/src/mmdb/mmdb_chain.h
lib/src/mmdb/mmdb_cifdefs.cpp
lib/src/mmdb/mmdb_cifdefs.h
lib/src/mmdb/mmdb_coormngr.cpp
lib/src/mmdb/mmdb_coormngr.h
lib/src/mmdb/mmdb_cryst.cpp
lib/src/mmdb/mmdb_cryst.h
lib/src/mmdb/mmdb_defs.h
lib/src/mmdb/mmdb_ficif.cpp
lib/src/mmdb/mmdb_ficif.h
lib/src/mmdb/mmdb_file.cpp
lib/src/mmdb/mmdb_file.h
lib/src/mmdb/mmdb_graph.cpp
lib/src/mmdb/mmdb_graph.h
lib/src/mmdb/mmdb_manager.cpp
lib/src/mmdb/mmdb_manager.h
lib/src/mmdb/mmdb_mask.cpp
lib/src/mmdb/mmdb_mask.h
lib/src/mmdb/mmdb_mmcif.cpp
lib/src/mmdb/mmdb_mmcif.h
lib/src/mmdb/mmdb_model.cpp
lib/src/mmdb/mmdb_model.h
lib/src/mmdb/mmdb_rwbrook.cpp
lib/src/mmdb/mmdb_rwbrook.h
lib/src/mmdb/mmdb_sbase.cpp
lib/src/mmdb/mmdb_sbase.h
lib/src/mmdb/mmdb_sbase0.cpp
lib/src/mmdb/mmdb_sbase0.h
lib/src/mmdb/mmdb_selmngr.cpp
lib/src/mmdb/mmdb_selmngr.h
lib/src/mmdb/mmdb_symop.cpp
lib/src/mmdb/mmdb_symop.h
lib/src/mmdb/mmdb_tables.cpp
lib/src/mmdb/mmdb_tables.h
lib/src/mmdb/mmdb_title.cpp
lib/src/mmdb/mmdb_title.h
lib/src/mmdb/mmdb_uddata.cpp
lib/src/mmdb/mmdb_uddata.h
lib/src/mmdb/mmdb_utils.cpp
lib/src/mmdb/mmdb_utils.h
lib/src/mmdb/mmdb_xml.cpp
lib/src/mmdb/mmdb_xml.h
lib/src/mmdb/random_n.cpp
lib/src/mmdb/random_n.h
lib/src/mmdb/stream_.cpp
lib/src/mmdb/stream_.h
lib/ssm/ss_csia.cpp
lib/ssm/ss_csia.h
lib/ssm/ss_graph.cpp
lib/ssm/ss_graph.h
lib/ssm/ss_vxedge.cpp
lib/ssm/ss_vxedge.h
lib/ssm/ssm_align.cpp
lib/ssm/ssm_align.h
lib/ssm/ssm_superpose.cpp
lib/ssm/ssm_superpose.h
""".splitlines()
  n_makedirs = 0
  n_copied = 0
  n_updated = 0
  n_already_up_to_date = 0
  for path in relative_paths:
    dir = op.split(path)[0]
    if (dir != "" and not op.isdir(dir)):
      os.makedirs(dir)
      n_makedirs += 1
    source = open(op.join(source_root, path), "rb").read()
    if (not op.isfile(path)):
      n_copied += 1
    else:
      target = open(path, "rb").read()
      if (target == source):
        n_already_up_to_date += 1
        source = None
      else:
        n_updated += 1
    if (source is not None):
      open(path, "wb").write(source)
  print "Directories created:", n_makedirs
  print "Files copied:", n_copied
  print "Files updated:", n_updated
  print "Files already up-to-date:", n_already_up_to_date
  print "Done."

if (__name__ == "__main__"):
  run(args=sys.argv[1:])
