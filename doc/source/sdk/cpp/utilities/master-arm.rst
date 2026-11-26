:orphan:

MasterArm (renamed)
===================

``rb::upc::MasterArm`` was renamed to ``rb::upc::LeaderArm`` in rby1-sdk
v0.10.0. ``MasterArm`` remains as a deprecated alias of ``LeaderArm``, and
``rby1-sdk/upc/master_arm.h`` remains as a deprecated header. New code should
use ``rb::upc::LeaderArm`` and ``rby1-sdk/upc/leader_arm.h``.

See :doc:`leader-arm`.
