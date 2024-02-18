// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cpln

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/pulumiverse/pulumi-cpln/sdk/go/cpln/internal"
)

type Gvc struct {
	pulumi.CustomResourceState

	Alias               pulumi.StringOutput             `pulumi:"alias"`
	ControlplaneTracing GvcControlplaneTracingPtrOutput `pulumi:"controlplaneTracing"`
	CplnId              pulumi.StringOutput             `pulumi:"cplnId"`
	Description         pulumi.StringPtrOutput          `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           pulumi.StringPtrOutput       `pulumi:"domain"`
	Env              pulumi.StringMapOutput       `pulumi:"env"`
	LightstepTracing GvcLightstepTracingPtrOutput `pulumi:"lightstepTracing"`
	LoadBalancer     GvcLoadBalancerPtrOutput     `pulumi:"loadBalancer"`
	Locations        pulumi.StringArrayOutput     `pulumi:"locations"`
	Name             pulumi.StringOutput          `pulumi:"name"`
	OtelTracing      GvcOtelTracingPtrOutput      `pulumi:"otelTracing"`
	PullSecrets      pulumi.StringArrayOutput     `pulumi:"pullSecrets"`
	SelfLink         pulumi.StringOutput          `pulumi:"selfLink"`
	Sidecar          GvcSidecarPtrOutput          `pulumi:"sidecar"`
	Tags             pulumi.StringMapOutput       `pulumi:"tags"`
}

// NewGvc registers a new resource with the given unique name, arguments, and options.
func NewGvc(ctx *pulumi.Context,
	name string, args *GvcArgs, opts ...pulumi.ResourceOption) (*Gvc, error) {
	if args == nil {
		args = &GvcArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Gvc
	err := ctx.RegisterResource("cpln:index/gvc:Gvc", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGvc gets an existing Gvc resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGvc(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GvcState, opts ...pulumi.ResourceOption) (*Gvc, error) {
	var resource Gvc
	err := ctx.ReadResource("cpln:index/gvc:Gvc", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Gvc resources.
type gvcState struct {
	Alias               *string                 `pulumi:"alias"`
	ControlplaneTracing *GvcControlplaneTracing `pulumi:"controlplaneTracing"`
	CplnId              *string                 `pulumi:"cplnId"`
	Description         *string                 `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           *string              `pulumi:"domain"`
	Env              map[string]string    `pulumi:"env"`
	LightstepTracing *GvcLightstepTracing `pulumi:"lightstepTracing"`
	LoadBalancer     *GvcLoadBalancer     `pulumi:"loadBalancer"`
	Locations        []string             `pulumi:"locations"`
	Name             *string              `pulumi:"name"`
	OtelTracing      *GvcOtelTracing      `pulumi:"otelTracing"`
	PullSecrets      []string             `pulumi:"pullSecrets"`
	SelfLink         *string              `pulumi:"selfLink"`
	Sidecar          *GvcSidecar          `pulumi:"sidecar"`
	Tags             map[string]string    `pulumi:"tags"`
}

type GvcState struct {
	Alias               pulumi.StringPtrInput
	ControlplaneTracing GvcControlplaneTracingPtrInput
	CplnId              pulumi.StringPtrInput
	Description         pulumi.StringPtrInput
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           pulumi.StringPtrInput
	Env              pulumi.StringMapInput
	LightstepTracing GvcLightstepTracingPtrInput
	LoadBalancer     GvcLoadBalancerPtrInput
	Locations        pulumi.StringArrayInput
	Name             pulumi.StringPtrInput
	OtelTracing      GvcOtelTracingPtrInput
	PullSecrets      pulumi.StringArrayInput
	SelfLink         pulumi.StringPtrInput
	Sidecar          GvcSidecarPtrInput
	Tags             pulumi.StringMapInput
}

func (GvcState) ElementType() reflect.Type {
	return reflect.TypeOf((*gvcState)(nil)).Elem()
}

type gvcArgs struct {
	ControlplaneTracing *GvcControlplaneTracing `pulumi:"controlplaneTracing"`
	Description         *string                 `pulumi:"description"`
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           *string              `pulumi:"domain"`
	Env              map[string]string    `pulumi:"env"`
	LightstepTracing *GvcLightstepTracing `pulumi:"lightstepTracing"`
	LoadBalancer     *GvcLoadBalancer     `pulumi:"loadBalancer"`
	Locations        []string             `pulumi:"locations"`
	Name             *string              `pulumi:"name"`
	OtelTracing      *GvcOtelTracing      `pulumi:"otelTracing"`
	PullSecrets      []string             `pulumi:"pullSecrets"`
	Sidecar          *GvcSidecar          `pulumi:"sidecar"`
	Tags             map[string]string    `pulumi:"tags"`
}

// The set of arguments for constructing a Gvc resource.
type GvcArgs struct {
	ControlplaneTracing GvcControlplaneTracingPtrInput
	Description         pulumi.StringPtrInput
	// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
	Domain           pulumi.StringPtrInput
	Env              pulumi.StringMapInput
	LightstepTracing GvcLightstepTracingPtrInput
	LoadBalancer     GvcLoadBalancerPtrInput
	Locations        pulumi.StringArrayInput
	Name             pulumi.StringPtrInput
	OtelTracing      GvcOtelTracingPtrInput
	PullSecrets      pulumi.StringArrayInput
	Sidecar          GvcSidecarPtrInput
	Tags             pulumi.StringMapInput
}

func (GvcArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gvcArgs)(nil)).Elem()
}

type GvcInput interface {
	pulumi.Input

	ToGvcOutput() GvcOutput
	ToGvcOutputWithContext(ctx context.Context) GvcOutput
}

func (*Gvc) ElementType() reflect.Type {
	return reflect.TypeOf((**Gvc)(nil)).Elem()
}

func (i *Gvc) ToGvcOutput() GvcOutput {
	return i.ToGvcOutputWithContext(context.Background())
}

func (i *Gvc) ToGvcOutputWithContext(ctx context.Context) GvcOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GvcOutput)
}

func (i *Gvc) ToOutput(ctx context.Context) pulumix.Output[*Gvc] {
	return pulumix.Output[*Gvc]{
		OutputState: i.ToGvcOutputWithContext(ctx).OutputState,
	}
}

// GvcArrayInput is an input type that accepts GvcArray and GvcArrayOutput values.
// You can construct a concrete instance of `GvcArrayInput` via:
//
//	GvcArray{ GvcArgs{...} }
type GvcArrayInput interface {
	pulumi.Input

	ToGvcArrayOutput() GvcArrayOutput
	ToGvcArrayOutputWithContext(context.Context) GvcArrayOutput
}

type GvcArray []GvcInput

func (GvcArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Gvc)(nil)).Elem()
}

func (i GvcArray) ToGvcArrayOutput() GvcArrayOutput {
	return i.ToGvcArrayOutputWithContext(context.Background())
}

func (i GvcArray) ToGvcArrayOutputWithContext(ctx context.Context) GvcArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GvcArrayOutput)
}

func (i GvcArray) ToOutput(ctx context.Context) pulumix.Output[[]*Gvc] {
	return pulumix.Output[[]*Gvc]{
		OutputState: i.ToGvcArrayOutputWithContext(ctx).OutputState,
	}
}

// GvcMapInput is an input type that accepts GvcMap and GvcMapOutput values.
// You can construct a concrete instance of `GvcMapInput` via:
//
//	GvcMap{ "key": GvcArgs{...} }
type GvcMapInput interface {
	pulumi.Input

	ToGvcMapOutput() GvcMapOutput
	ToGvcMapOutputWithContext(context.Context) GvcMapOutput
}

type GvcMap map[string]GvcInput

func (GvcMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Gvc)(nil)).Elem()
}

func (i GvcMap) ToGvcMapOutput() GvcMapOutput {
	return i.ToGvcMapOutputWithContext(context.Background())
}

func (i GvcMap) ToGvcMapOutputWithContext(ctx context.Context) GvcMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GvcMapOutput)
}

func (i GvcMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Gvc] {
	return pulumix.Output[map[string]*Gvc]{
		OutputState: i.ToGvcMapOutputWithContext(ctx).OutputState,
	}
}

type GvcOutput struct{ *pulumi.OutputState }

func (GvcOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Gvc)(nil)).Elem()
}

func (o GvcOutput) ToGvcOutput() GvcOutput {
	return o
}

func (o GvcOutput) ToGvcOutputWithContext(ctx context.Context) GvcOutput {
	return o
}

func (o GvcOutput) ToOutput(ctx context.Context) pulumix.Output[*Gvc] {
	return pulumix.Output[*Gvc]{
		OutputState: o.OutputState,
	}
}

func (o GvcOutput) Alias() pulumi.StringOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringOutput { return v.Alias }).(pulumi.StringOutput)
}

func (o GvcOutput) ControlplaneTracing() GvcControlplaneTracingPtrOutput {
	return o.ApplyT(func(v *Gvc) GvcControlplaneTracingPtrOutput { return v.ControlplaneTracing }).(GvcControlplaneTracingPtrOutput)
}

func (o GvcOutput) CplnId() pulumi.StringOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringOutput { return v.CplnId }).(pulumi.StringOutput)
}

func (o GvcOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Deprecated: Selecting a domain on a GVC will be deprecated in the future. Use the 'cpln_domain resource' instead.
func (o GvcOutput) Domain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringPtrOutput { return v.Domain }).(pulumi.StringPtrOutput)
}

func (o GvcOutput) Env() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringMapOutput { return v.Env }).(pulumi.StringMapOutput)
}

func (o GvcOutput) LightstepTracing() GvcLightstepTracingPtrOutput {
	return o.ApplyT(func(v *Gvc) GvcLightstepTracingPtrOutput { return v.LightstepTracing }).(GvcLightstepTracingPtrOutput)
}

func (o GvcOutput) LoadBalancer() GvcLoadBalancerPtrOutput {
	return o.ApplyT(func(v *Gvc) GvcLoadBalancerPtrOutput { return v.LoadBalancer }).(GvcLoadBalancerPtrOutput)
}

func (o GvcOutput) Locations() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringArrayOutput { return v.Locations }).(pulumi.StringArrayOutput)
}

func (o GvcOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o GvcOutput) OtelTracing() GvcOtelTracingPtrOutput {
	return o.ApplyT(func(v *Gvc) GvcOtelTracingPtrOutput { return v.OtelTracing }).(GvcOtelTracingPtrOutput)
}

func (o GvcOutput) PullSecrets() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringArrayOutput { return v.PullSecrets }).(pulumi.StringArrayOutput)
}

func (o GvcOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringOutput { return v.SelfLink }).(pulumi.StringOutput)
}

func (o GvcOutput) Sidecar() GvcSidecarPtrOutput {
	return o.ApplyT(func(v *Gvc) GvcSidecarPtrOutput { return v.Sidecar }).(GvcSidecarPtrOutput)
}

func (o GvcOutput) Tags() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Gvc) pulumi.StringMapOutput { return v.Tags }).(pulumi.StringMapOutput)
}

type GvcArrayOutput struct{ *pulumi.OutputState }

func (GvcArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Gvc)(nil)).Elem()
}

func (o GvcArrayOutput) ToGvcArrayOutput() GvcArrayOutput {
	return o
}

func (o GvcArrayOutput) ToGvcArrayOutputWithContext(ctx context.Context) GvcArrayOutput {
	return o
}

func (o GvcArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Gvc] {
	return pulumix.Output[[]*Gvc]{
		OutputState: o.OutputState,
	}
}

func (o GvcArrayOutput) Index(i pulumi.IntInput) GvcOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Gvc {
		return vs[0].([]*Gvc)[vs[1].(int)]
	}).(GvcOutput)
}

type GvcMapOutput struct{ *pulumi.OutputState }

func (GvcMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Gvc)(nil)).Elem()
}

func (o GvcMapOutput) ToGvcMapOutput() GvcMapOutput {
	return o
}

func (o GvcMapOutput) ToGvcMapOutputWithContext(ctx context.Context) GvcMapOutput {
	return o
}

func (o GvcMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Gvc] {
	return pulumix.Output[map[string]*Gvc]{
		OutputState: o.OutputState,
	}
}

func (o GvcMapOutput) MapIndex(k pulumi.StringInput) GvcOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Gvc {
		return vs[0].(map[string]*Gvc)[vs[1].(string)]
	}).(GvcOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GvcInput)(nil)).Elem(), &Gvc{})
	pulumi.RegisterInputType(reflect.TypeOf((*GvcArrayInput)(nil)).Elem(), GvcArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GvcMapInput)(nil)).Elem(), GvcMap{})
	pulumi.RegisterOutputType(GvcOutput{})
	pulumi.RegisterOutputType(GvcArrayOutput{})
	pulumi.RegisterOutputType(GvcMapOutput{})
}
