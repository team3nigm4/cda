# Apply openGL functions glUniform... more easily

import OpenGL.GL as gl

def glUniformv(shader, name, value1):
	shader.use()
	gl.glUniformMatrix4fv(shader.getLink(name), 1, gl.GL_FALSE, value1)

def glUniformf(shader, name, value):
	shader.use()
	gl.glUniform1f(shader.getLink(name), value)
