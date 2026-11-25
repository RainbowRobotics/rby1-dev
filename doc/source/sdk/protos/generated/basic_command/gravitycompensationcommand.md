(rb-api-gravitycompensationcommand)=
# GravityCompensationCommand

- Source proto: `rb/api/basic_command.proto`

Free-drive (hand-guiding) mode for the selected joints: position feedback is faded out, so the joints can be moved by hand and do NOT hold their pose against external forces or payloads. When the command ends (control hold time expires or it is cancelled), position feedback fades back in and the joints hold the pose they are in at that moment.

```{warning}
Do not use this command to hold a pose. Support the arm before you start it: the joints can move or sag when the actual load (for example, a payload or a tool) differs from the robot model.
```


## Subtypes

- [GravityCompensationCommand.Feedback](gravitycompensationcommand-feedback.md)
- [GravityCompensationCommand.Request](gravitycompensationcommand-request.md)

