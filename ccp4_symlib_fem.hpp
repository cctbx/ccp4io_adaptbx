#ifndef CCP4IO_ADAPTBX_CCP4_SYMLIB_FEM_HPP
#define CCP4IO_ADAPTBX_CCP4_SYMLIB_FEM_HPP

#include <fem.hpp> // Fortran EMulation library of fable module

extern "C" {

typedef unsigned int ccp4_ftn_logical;

void
symfr2_(
  const char* icol,
  int const* i1,
  int* ns,
  float* rot, // [][4][4]
  int icol_len);

void
msymlb_(
  int const* ist,
  int* lspgrp,
  char* namspg,
  char* nampg,
  int* nsymp,
  int* nsym,
  float* rot, // [][4][4]
  int namspg_len,
  int nampg_len);

void
symtr3_(
  int const* nsm,
  /*arr_cref<float, 3>*/ float const* rsm,
  /*str_arr_ref<>*/ char* symchs,
  int const* iprint,
  int symchs_len);

void
asuset_(
  const char* spgnam,
  int const* numsgp,
  char* pgname,
  int const* msym,
  float* rrsym, // [][4][4]
  int* msymp,
  int* mlaue,
  ccp4_ftn_logical const* lprint,
  int spgnam_len,
  int pgname_len);

void
asuput_(
  int const* ihkl,
  int* jhkl,
  int* isym);

void
asuget_(
  int const* ihkl,
  int* jhkl,
  int const* isym);

void
centric_(
  int const* nsm,
  /*arr_cref<float, 3>*/ float const* rsm,
  int const* iprint);

void
centr_(
  int const* hkl,
  int* ic);

void
setrsl_(
  float const* a,
  float const* b,
  float const* c,
  float const* alpha,
  float const* beta,
  float const* gamma);

void
sthlsq1_(
  float* reso,
  int const* ih,
  int const* ik,
  int const* il);

} // extern "C"

namespace ccp4_symlib_fem {

using namespace fem::major_types;

inline
void
symfr2(
  str_cref icol,
  int const& i1,
  int& ns,
  arr_ref<float, 3> rot)
{
  symfr2_(
    icol.elems(),
    &i1,
    &ns,
    rot.begin(),
    icol.len());
}

inline
void
msymlb(
  int const& ist,
  int& lspgrp,
  str_ref namspg,
  str_ref nampg,
  int& nsymp,
  int& nsym,
  arr_ref<float, 3> rot)
{
  msymlb_(
    &ist, &lspgrp, namspg.elems(), nampg.elems(), &nsymp, &nsym, rot.begin(),
    namspg.len(), nampg.len());
}

inline
void
msymlb3(
  int const& ist,
  int& lspgrp,
  str_ref namspg_cif,
  str_ref namspg_cifs,
  str_ref nampg,
  int& nsymp,
  int& nsym,
  arr_ref<float, 3> rlsymmmatrx)
{
  throw TBXX_NOT_IMPLEMENTED();
}

inline
void
symtr3(
  int const& nsm,
  arr_cref<float, 3> rsm,
  str_arr_ref<> symchs,
  int const& iprint)
{
  symtr3_(&nsm, rsm.begin(), symchs.begin(), &iprint, symchs.len());
}

inline
void
asuset(
  str_cref spgnam,
  int const& numsgp,
  str_ref pgname,
  int const& msym,
  arr_ref<float, 3> rrsym,
  int& msymp,
  int& mlaue,
  bool const& lprint)
{
  ccp4_ftn_logical lprint_ = lprint;
  asuset_(
    spgnam.elems(),
    &numsgp,
    pgname.elems(),
    &msym,
    rrsym.begin(),
    &msymp,
    &mlaue,
    &lprint_,
    spgnam.len(),
    pgname.len());
}

inline
void
asuput(
  arr_cref<int> ihkl,
  arr_ref<int> jhkl,
  int& isym)
{
  asuput_(ihkl.begin(), jhkl.begin(), &isym);
}

inline
void
asuget(
  arr_cref<int> ihkl,
  arr_ref<int> jhkl,
  int const& isym)
{
  asuget_(ihkl.begin(), jhkl.begin(), &isym);
}

inline
void
centric(
  int const& nsm,
  arr_cref<float, 3> rsm,
  int const& iprint)
{
  centric_(&nsm, rsm.begin(), &iprint);
}

inline
void
centr(
  arr_cref<int> hkl,
  int& ic)
{
  centr_(hkl.begin(), &ic);
}

inline
void
setrsl(
  float const& a,
  float const& b,
  float const& c,
  float const& alpha,
  float const& beta,
  float const& gamma)
{
  setrsl_(&a, &b, &c, &alpha, &beta, &gamma);
}

inline
float
sthlsq(
  int const& ih,
  int const& ik,
  int const& il)
{
  float reso;
  sthlsq1_(&reso, &ih, &ik, &il);
  return reso;
}

} // namespace ccp4_symlib_fem

#endif // GUARD
