import syft as sy
import torch as th
import syft.frameworks.tenseal as ts

hook = sy.TorchHook(th)
pub, pri =ts.generate_ckks_keys()
x = th.tensor([1.8, 1.2 , 4.2]).encrypt('ckks', public_keys = pub)
y = th.tensor([2.0, 2.0 , 2.0]).encrypt('ckks', public_keys = pub)

encrypted_add = x+y
encrypted_sub = x-y
encrypted_mul = x*y

encrypted_add.decrypt('ckks', private_key=pri)
encrypted_sub.decrypt('ckks', private_key=pri)
encrypted_mul.decrypt('ckks', private_key=pri)
