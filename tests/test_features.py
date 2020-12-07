
# A grab-bag of features
from bosmer import Migration


class Migration_2020_12_06_1(Migration):
  def change(self):
    self.move("/blah/*", "/blah2/*")

class Migration_2020_12_06_2(Migration):
  def change(self):
    self.copy("/blah/*", "/blah2/*")

class Migration_2020_12_06_3(Migration):
  def change(self):
    self.copy_and_alter()

class Migration_2020_12_06_4(Migration):
  def up(self):
    def some_fn():
      pass
    self.alter_each("/haha/what/*", some_fn)

  def down(self):
    def some_fn():
      pass
    self.alter_each("/haha/what/*", some_fn)
  
class Migration_2020_12_06_5(Migration):
  backup = True
  backup_ttl_days = 365

  def up(self):
    self.delete("/blah/hehe")
  
  def down(self):
    self.restore_from_backup()
