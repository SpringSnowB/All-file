import struct
#i整型，4s  4个字节串（多的截取，少的补0的编码），f浮点型
st = struct.Struct('i4sif')
data = st.pack(*(1,b'mary',55,8.6))
print(data)
st = struct.Struct('i3sif')
print(st.unpack(data))