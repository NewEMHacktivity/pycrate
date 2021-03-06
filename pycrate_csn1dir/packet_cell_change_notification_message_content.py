# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.3
# *
# * Copyright 2018. Benoit Michau. ANSSI. P1sec.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_csn1dir/packet_cell_change_notification_message_content.py
# * Created : 2018-11-21
# * Authors : Benoit Michau
# *--------------------------------------------------------
#*/
# specification: TS 44.060 - d60
# section: 11.2.3a Packet Cell Change Notification
# top-level object: Packet Cell Change Notification message content

# external references
from pycrate_csn1dir.padding_bits import padding_bits
from pycrate_csn1dir.utran_csg_measurement_report_ie import utran_csg_measurement_report_ie
from pycrate_csn1dir.global_tfi_ie import global_tfi_ie
from pycrate_csn1dir.e_utran_csg_measurement_report_ie import e_utran_csg_measurement_report_ie

# code automatically generated by pycrate_csn1
# change object type with type=CSN1T_BSTR (default type is CSN1T_UINT) in init
# add dict for value interpretation with dic={...} in CSN1Bit init
# add dict for key interpretation with kdic={...} in CSN1Alt init

from pycrate_csn1.csnobj import *

e_utran_target_cell_with_extended_earfcn_struct = CSN1List(name='e_utran_target_cell_with_extended_earfcn_struct', list=[
  CSN1Bit(name='earfcn_extended', bit=18),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='measurement_bandwidth', bit=3)])}),
  CSN1Bit(name='physical_layer_cell_identity', bit=9),
  CSN1Bit(name='reporting_quantity', bit=6)])

_3g_target_cell_struct = CSN1List(name='_3g_target_cell_struct', list=[
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='fdd_arfcn', bit=14),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bandwidth_fdd', bit=3)])}),
    CSN1Bit(name='scrambling_code', bit=9)])}),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='tdd_arfcn', bit=14),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bandwidth_tdd', bit=3)])}),
    CSN1Bit(name='cell_parameter', bit=7),
    CSN1Bit(name='sync_case')])}),
  CSN1Bit(name='reporting_quantity', bit=6)])

ccn_measurement_report_struct = CSN1List(name='ccn_measurement_report_struct', list=[
  CSN1Bit(name='rxlev_serving_cell', bit=6),
  CSN1Val(name='', val='0'),
  CSN1Bit(name='number_of_nc_measurements', bit=3),
  CSN1List(num=([2], lambda x: x), list=[
    CSN1Bit(name='frequency_n', bit=6),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='bsic_n', bit=6)])}),
    CSN1Bit(name='rxlev_n', bit=6)])])

e_utran_target_cell_struct = CSN1List(name='e_utran_target_cell_struct', list=[
  CSN1Bit(name='earfcn', bit=16),
  CSN1Alt(alt={
    '0': ('', []),
    '1': ('', [
    CSN1Bit(name='measurement_bandwidth', bit=3)])}),
  CSN1Bit(name='physical_layer_cell_identity', bit=9),
  CSN1Bit(name='reporting_quantity', bit=6)])

_3g_ccn_measurement_report_struct = CSN1List(name='_3g_ccn_measurement_report_struct', list=[
  CSN1Bit(name='n_3g', bit=3),
  CSN1List(num=([0], lambda x: x + 1), list=[
    CSN1Bit(name='_3g_cell_list_index', bit=7),
    CSN1Bit(name='reporting_quantity', bit=6)])])

e_utran_ccn_measurement_report_struct = CSN1List(name='e_utran_ccn_measurement_report_struct', list=[
  CSN1Bit(name='_3g_ba_used'),
  CSN1Bit(name='n_e_utran', bit=2),
  CSN1List(num=([1], lambda x: x + 1), list=[
    CSN1Bit(name='e_utran_frequency_index', bit=3),
    CSN1Bit(name='cell_identity', bit=9),
    CSN1Bit(name='reporting_quantity', bit=6)])])

packet_cell_change_notification_message_content = CSN1List(name='packet_cell_change_notification_message_content', list=[
  CSN1Ref(name='global_tfi', obj=global_tfi_ie),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='arfcn', bit=10),
    CSN1Bit(name='bsic', bit=6)]),
    '10': ('', [
    CSN1Ref(name='_3g_target_cell', obj=_3g_target_cell_struct)]),
    '110': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='arfcn', bit=10),
      CSN1Bit(name='bsic', bit=6)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='_3g_target_cell', obj=_3g_target_cell_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='e_utran_target_cell', obj=e_utran_target_cell_struct)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='e_utran_ccn_measurement_report', obj=e_utran_ccn_measurement_report_struct)])})]),
    '1110': ('', [
    CSN1Alt(alt={
      '0': ('', [
      CSN1Ref(name='utran_csg_target_cell_measurement_report', obj=utran_csg_measurement_report_ie)]),
      '1': ('', [
      CSN1Ref(name='e_utran_csg_target_cell_measurement_report', obj=e_utran_csg_measurement_report_ie)])}),
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Ref(name='e_utran_ccn_measurement_report', obj=e_utran_ccn_measurement_report_struct)])})])}),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(name='ba_used')]),
    '1': ('', [
    CSN1Bit(name='psi3_change_mark', bit=2)])}),
  CSN1Bit(name='pmo_used'),
  CSN1Bit(name='pccn_sending'),
  CSN1Ref(name='ccn_measurement_report', obj=ccn_measurement_report_struct),
  CSN1Alt(alt={
    '0': ('', [
    CSN1Bit(bit=-1)]),
    '1': ('', [
    CSN1Alt(alt={
      '0': ('', []),
      '1': ('', [
      CSN1Bit(name='_3g_ba_used')])}),
    CSN1Ref(name='_3g_ccn_measurement_report', obj=_3g_ccn_measurement_report_struct),
    CSN1Alt(alt={
      '0': ('', [
      CSN1Bit(bit=-1)]),
      '1': ('', [
      CSN1Bit(name='csg_discriminator'),
      CSN1Alt(alt={
        '0': ('', [
        CSN1Bit(bit=-1)]),
        '1': ('', [
        CSN1Alt(alt={
          '0': ('', []),
          '1': ('', [
          CSN1Ref(name='e_utran_target_cell_with_extended_earfcn', obj=e_utran_target_cell_with_extended_earfcn_struct)])}),
        CSN1Alt(alt={
          '0': ('', [
          CSN1Bit(bit=-1)]),
          '1': ('', [
          CSN1Alt(alt={
            '0': ('', []),
            '1': ('', [
            CSN1Bit(name='downlink_etfi', bit=3)])}),
          CSN1Ref(obj=padding_bits)]),
          None: ('', [])})]),
        None: ('', [])})]),
      None: ('', [])})]),
    None: ('', [])})])

