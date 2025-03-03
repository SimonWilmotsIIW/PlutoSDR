import pmt
key0 = pmt.intern("rf_bandwidth")
val0 = pmt.intern("23000000")
msg_dic = pmt.make_dict()
msg_dic = pmt.dict_add(msg_dic, key0, val0)